# EMA Hourly Continuation — ONE/USDT P26_34

**Symbol:** ONE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 169 |
| net_profit_factor | 0.8810 |
| net_win_rate | 0.5444 |
| gross_profit_factor | 1.1848 |
| gross_win_rate | 0.5444 |
| sharpe_ratio | -0.4795 |
| sortino_ratio | -0.0904 |
| max_drawdown | 0.1759 |
| cagr | -0.0420 |
| net_avg_win | 82.1057 |
| net_avg_loss | -111.3529 |
| avg_hold_time_bars | 5.2130 |
| exposure | 0.0400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
