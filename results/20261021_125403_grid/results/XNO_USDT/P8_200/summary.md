# EMA Hourly Continuation — XNO/USDT P8_200

**Symbol:** XNO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.7039 |
| net_win_rate | 0.4486 |
| gross_profit_factor | 0.8432 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -2.5491 |
| sortino_ratio | -0.7467 |
| max_drawdown | 0.5793 |
| cagr | -0.2916 |
| net_avg_win | 71.7266 |
| net_avg_loss | -82.9017 |
| avg_hold_time_bars | 36.6425 |
| exposure | 0.7129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
