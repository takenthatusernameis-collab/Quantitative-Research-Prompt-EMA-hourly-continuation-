# EMA Hourly Continuation — IMX/USDT P12_100

**Symbol:** IMX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.8692 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.0333 |
| gross_win_rate | 0.5139 |
| sharpe_ratio | -0.8127 |
| sortino_ratio | -0.2610 |
| max_drawdown | 0.3900 |
| cagr | -0.1171 |
| net_avg_win | 69.4618 |
| net_avg_loss | -84.4974 |
| avg_hold_time_bars | 23.6255 |
| exposure | 0.5367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
