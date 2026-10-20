# EMA Hourly Continuation — EDU/USDT P8_89

**Symbol:** EDU/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.6345 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.8778 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -4.0439 |
| sortino_ratio | -1.5353 |
| max_drawdown | 0.8467 |
| cagr | -0.5162 |
| net_avg_win | 43.5164 |
| net_avg_loss | -58.0207 |
| avg_hold_time_bars | 19.8714 |
| exposure | 0.6573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
