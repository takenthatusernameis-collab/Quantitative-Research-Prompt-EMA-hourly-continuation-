# EMA Hourly Continuation — 1INCH/USDT P20_89

**Symbol:** 1INCH/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.5104 |
| net_win_rate | 0.4426 |
| gross_profit_factor | 0.8378 |
| gross_win_rate | 0.4523 |
| sharpe_ratio | -6.0271 |
| sortino_ratio | -2.2777 |
| max_drawdown | 0.9402 |
| cagr | -0.6696 |
| net_avg_win | 30.5571 |
| net_avg_loss | -47.5398 |
| avg_hold_time_bars | 13.1618 |
| exposure | 0.4325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
