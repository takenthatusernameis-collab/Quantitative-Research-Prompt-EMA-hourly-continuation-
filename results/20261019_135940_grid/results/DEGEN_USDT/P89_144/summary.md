# EMA Hourly Continuation — DEGEN/USDT P89_144

**Symbol:** DEGEN/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.7280 |
| net_win_rate | 0.5066 |
| gross_profit_factor | 1.0994 |
| gross_win_rate | 0.5132 |
| sharpe_ratio | -2.6376 |
| sortino_ratio | -0.7921 |
| max_drawdown | 0.6417 |
| cagr | -0.3178 |
| net_avg_win | 71.7785 |
| net_avg_loss | -101.2328 |
| avg_hold_time_bars | 6.1674 |
| exposure | 0.1275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
