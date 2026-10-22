# EMA Hourly Continuation — KNC/USDT P8_144

**Symbol:** KNC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.7871 |
| net_win_rate | 0.4955 |
| gross_profit_factor | 0.9775 |
| gross_win_rate | 0.4955 |
| sharpe_ratio | -1.3424 |
| sortino_ratio | -0.3511 |
| max_drawdown | 0.3584 |
| cagr | -0.1496 |
| net_avg_win | 74.4599 |
| net_avg_loss | -92.9210 |
| avg_hold_time_bars | 51.9015 |
| exposure | 0.7903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
