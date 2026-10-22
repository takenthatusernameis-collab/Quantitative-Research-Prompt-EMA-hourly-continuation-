# EMA Hourly Continuation — SKY/USDT P100_144

**Symbol:** SKY/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.5212 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.9816 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -4.9781 |
| sortino_ratio | -1.5712 |
| max_drawdown | 0.8188 |
| cagr | -0.5369 |
| net_avg_win | 44.9615 |
| net_avg_loss | -77.7669 |
| avg_hold_time_bars | 4.1605 |
| exposure | 0.0940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
