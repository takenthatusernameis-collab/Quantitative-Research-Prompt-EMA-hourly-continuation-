# EMA Hourly Continuation — ONT/USDT P50_144

**Symbol:** ONT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.5634 |
| net_win_rate | 0.4657 |
| gross_profit_factor | 0.8498 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -3.5837 |
| sortino_ratio | -1.1113 |
| max_drawdown | 0.7344 |
| cagr | -0.4066 |
| net_avg_win | 42.1565 |
| net_avg_loss | -65.2216 |
| avg_hold_time_bars | 13.0249 |
| exposure | 0.2835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
