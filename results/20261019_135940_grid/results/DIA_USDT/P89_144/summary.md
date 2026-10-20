# EMA Hourly Continuation — DIA/USDT P89_144

**Symbol:** DIA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.5721 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 1.0133 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -4.1122 |
| sortino_ratio | -1.2835 |
| max_drawdown | 0.7930 |
| cagr | -0.4550 |
| net_avg_win | 45.3674 |
| net_avg_loss | -71.5502 |
| avg_hold_time_bars | 6.0575 |
| exposure | 0.1335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
