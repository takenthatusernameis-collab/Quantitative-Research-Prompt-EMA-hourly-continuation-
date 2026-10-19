# EMA Hourly Continuation — SEI/USDT P50_144

**Symbol:** SEI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.6199 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.8730 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -3.3425 |
| sortino_ratio | -0.9955 |
| max_drawdown | 0.7023 |
| cagr | -0.3777 |
| net_avg_win | 55.1133 |
| net_avg_loss | -75.6822 |
| avg_hold_time_bars | 13.4442 |
| exposure | 0.2738 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
