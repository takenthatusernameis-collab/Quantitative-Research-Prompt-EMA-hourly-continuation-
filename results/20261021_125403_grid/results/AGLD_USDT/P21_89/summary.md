# EMA Hourly Continuation — AGLD/USDT P21_89

**Symbol:** AGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.7305 |
| net_win_rate | 0.4668 |
| gross_profit_factor | 0.9177 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -2.7622 |
| sortino_ratio | -0.9252 |
| max_drawdown | 0.7207 |
| cagr | -0.3467 |
| net_avg_win | 68.6444 |
| net_avg_loss | -82.2595 |
| avg_hold_time_bars | 15.0144 |
| exposure | 0.3785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
