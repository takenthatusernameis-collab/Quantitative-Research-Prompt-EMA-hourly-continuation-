# EMA Hourly Continuation — DEGEN/USDT P8_100

**Symbol:** DEGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.7892 |
| net_win_rate | 0.4963 |
| gross_profit_factor | 1.0165 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -2.0058 |
| sortino_ratio | -0.6543 |
| max_drawdown | 0.5581 |
| cagr | -0.2678 |
| net_avg_win | 76.6326 |
| net_avg_loss | -95.6538 |
| avg_hold_time_bars | 28.9082 |
| exposure | 0.7028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
