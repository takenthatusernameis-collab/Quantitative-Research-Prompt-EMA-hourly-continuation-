# EMA Hourly Continuation — YFI/USDT P50_55

**Symbol:** YFI/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 185 |
| net_profit_factor | 0.5209 |
| net_win_rate | 0.4703 |
| gross_profit_factor | 0.9205 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -2.7353 |
| sortino_ratio | -0.5359 |
| max_drawdown | 0.4759 |
| cagr | -0.2183 |
| net_avg_win | 57.8274 |
| net_avg_loss | -98.5500 |
| avg_hold_time_bars | 4.7946 |
| exposure | 0.0401 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
