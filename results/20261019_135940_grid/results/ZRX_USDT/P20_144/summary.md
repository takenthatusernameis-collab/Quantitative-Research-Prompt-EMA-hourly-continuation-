# EMA Hourly Continuation — ZRX/USDT P20_144

**Symbol:** ZRX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.5785 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8518 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -4.0745 |
| sortino_ratio | -1.2966 |
| max_drawdown | 0.8071 |
| cagr | -0.4734 |
| net_avg_win | 46.1386 |
| net_avg_loss | -66.1427 |
| avg_hold_time_bars | 22.4400 |
| exposure | 0.5355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
