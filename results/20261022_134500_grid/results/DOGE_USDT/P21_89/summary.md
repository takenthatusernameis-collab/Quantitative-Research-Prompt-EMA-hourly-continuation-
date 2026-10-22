# EMA Hourly Continuation — DOGE/USDT P21_89

**Symbol:** DOGE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.5337 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.8824 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -5.4272 |
| sortino_ratio | -1.9945 |
| max_drawdown | 0.9140 |
| cagr | -0.6182 |
| net_avg_win | 33.7443 |
| net_avg_loss | -52.3748 |
| avg_hold_time_bars | 12.1540 |
| exposure | 0.3768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
