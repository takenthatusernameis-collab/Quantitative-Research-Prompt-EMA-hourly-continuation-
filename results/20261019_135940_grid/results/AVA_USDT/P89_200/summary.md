# EMA Hourly Continuation — AVA/USDT P89_200

**Symbol:** AVA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.6102 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 0.9244 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -2.7417 |
| sortino_ratio | -0.7704 |
| max_drawdown | 0.6152 |
| cagr | -0.3092 |
| net_avg_win | 48.5575 |
| net_avg_loss | -76.8236 |
| avg_hold_time_bars | 10.6398 |
| exposure | 0.1920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
