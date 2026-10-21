# EMA Hourly Continuation — AVAX/USDT P20_26

**Symbol:** AVAX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 143 |
| net_profit_factor | 0.6703 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 0.9741 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -1.5594 |
| sortino_ratio | -0.2679 |
| max_drawdown | 0.3077 |
| cagr | -0.1151 |
| net_avg_win | 76.8243 |
| net_avg_loss | -109.8967 |
| avg_hold_time_bars | 4.2797 |
| exposure | 0.0278 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
