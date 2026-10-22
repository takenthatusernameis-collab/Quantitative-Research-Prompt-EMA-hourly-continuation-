# EMA Hourly Continuation — ONE/USDT P20_34

**Symbol:** ONE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.8711 |
| net_win_rate | 0.5400 |
| gross_profit_factor | 1.1634 |
| gross_win_rate | 0.5400 |
| sharpe_ratio | -0.7030 |
| sortino_ratio | -0.1764 |
| max_drawdown | 0.2689 |
| cagr | -0.0797 |
| net_avg_win | 78.4926 |
| net_avg_loss | -105.7834 |
| avg_hold_time_bars | 5.3733 |
| exposure | 0.0733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
