# EMA Hourly Continuation — JUP/USDT P50_144

**Symbol:** JUP/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.7541 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9089 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -1.5636 |
| sortino_ratio | -0.4075 |
| max_drawdown | 0.4074 |
| cagr | -0.1708 |
| net_avg_win | 71.4834 |
| net_avg_loss | -87.7115 |
| avg_hold_time_bars | 14.8687 |
| exposure | 0.2264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
