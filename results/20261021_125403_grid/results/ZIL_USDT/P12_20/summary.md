# EMA Hourly Continuation — ZIL/USDT P12_20

**Symbol:** ZIL/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.6889 |
| net_win_rate | 0.5031 |
| gross_profit_factor | 1.0410 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -2.2604 |
| sortino_ratio | -0.5879 |
| max_drawdown | 0.5268 |
| cagr | -0.2351 |
| net_avg_win | 66.1288 |
| net_avg_loss | -97.1836 |
| avg_hold_time_bars | 4.8773 |
| exposure | 0.0723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
