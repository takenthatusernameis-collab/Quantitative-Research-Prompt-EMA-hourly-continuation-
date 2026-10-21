# EMA Hourly Continuation — DCR/USDT P21_89

**Symbol:** DCR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.6839 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9045 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -2.5063 |
| sortino_ratio | -0.8411 |
| max_drawdown | 0.6547 |
| cagr | -0.3218 |
| net_avg_win | 50.2302 |
| net_avg_loss | -68.8411 |
| avg_hold_time_bars | 13.8435 |
| exposure | 0.3483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
