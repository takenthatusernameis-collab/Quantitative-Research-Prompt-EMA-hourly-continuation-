# EMA Hourly Continuation — TAO/USDT P21_34

**Symbol:** TAO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 219 |
| net_profit_factor | 0.7235 |
| net_win_rate | 0.4703 |
| gross_profit_factor | 0.9302 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -1.7386 |
| sortino_ratio | -0.3670 |
| max_drawdown | 0.4368 |
| cagr | -0.1555 |
| net_avg_win | 87.8655 |
| net_avg_loss | -107.8418 |
| avg_hold_time_bars | 5.4110 |
| exposure | 0.0539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
