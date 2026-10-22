# EMA Hourly Continuation — IOST/USDT P89_144

**Symbol:** IOST/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.8120 |
| net_win_rate | 0.5491 |
| gross_profit_factor | 1.2053 |
| gross_win_rate | 0.5491 |
| sharpe_ratio | -1.1349 |
| sortino_ratio | -0.2971 |
| max_drawdown | 0.3122 |
| cagr | -0.1280 |
| net_avg_win | 70.2280 |
| net_avg_loss | -105.3196 |
| avg_hold_time_bars | 7.0184 |
| exposure | 0.1040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
