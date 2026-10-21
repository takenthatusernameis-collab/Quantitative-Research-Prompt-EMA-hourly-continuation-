# EMA Hourly Continuation — CFG/USDT P89_100

**Symbol:** CFG/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 110 |
| net_profit_factor | 0.6326 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8529 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -1.5540 |
| sortino_ratio | -0.2322 |
| max_drawdown | 0.2893 |
| cagr | -0.1007 |
| net_avg_win | 80.5866 |
| net_avg_loss | -106.1534 |
| avg_hold_time_bars | 5.2000 |
| exposure | 0.0260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
