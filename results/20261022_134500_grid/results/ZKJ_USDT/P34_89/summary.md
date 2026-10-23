# EMA Hourly Continuation — ZKJ/USDT P34_89

**Symbol:** ZKJ/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.1386 |
| net_win_rate | 0.2494 |
| gross_profit_factor | 0.4148 |
| gross_win_rate | 0.3506 |
| sharpe_ratio | -10.9482 |
| sortino_ratio | -3.4587 |
| max_drawdown | 0.9911 |
| cagr | -0.8460 |
| net_avg_win | 15.0392 |
| net_avg_loss | -36.0597 |
| avg_hold_time_bars | 37.3247 |
| exposure | 0.7210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
