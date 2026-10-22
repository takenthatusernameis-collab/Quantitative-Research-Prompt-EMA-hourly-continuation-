# EMA Hourly Continuation — GMT/USDT P12_89

**Symbol:** GMT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.7271 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.8962 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -2.2971 |
| sortino_ratio | -0.7406 |
| max_drawdown | 0.5922 |
| cagr | -0.2890 |
| net_avg_win | 63.3534 |
| net_avg_loss | -77.8066 |
| avg_hold_time_bars | 22.1715 |
| exposure | 0.5170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
