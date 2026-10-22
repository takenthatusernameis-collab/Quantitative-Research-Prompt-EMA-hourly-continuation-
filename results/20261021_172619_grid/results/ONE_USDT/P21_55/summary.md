# EMA Hourly Continuation — ONE/USDT P21_55

**Symbol:** ONE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.7748 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 0.9831 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -1.8175 |
| sortino_ratio | -0.5744 |
| max_drawdown | 0.5365 |
| cagr | -0.2326 |
| net_avg_win | 69.3311 |
| net_avg_loss | -87.6621 |
| avg_hold_time_bars | 9.9836 |
| exposure | 0.2210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
