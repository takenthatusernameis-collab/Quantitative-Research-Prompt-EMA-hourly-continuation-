# EMA Hourly Continuation — IOST/USDT P12_34

**Symbol:** IOST/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1195 |
| net_profit_factor | 0.3946 |
| net_win_rate | 0.4402 |
| gross_profit_factor | 0.8905 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -8.9680 |
| sortino_ratio | -4.3631 |
| max_drawdown | 0.9959 |
| cagr | -0.8867 |
| net_avg_win | 12.3415 |
| net_avg_loss | -24.5882 |
| avg_hold_time_bars | 5.2912 |
| exposure | 0.2874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
