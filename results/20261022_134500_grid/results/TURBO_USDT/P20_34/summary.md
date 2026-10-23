# EMA Hourly Continuation — TURBO/USDT P20_34

**Symbol:** TURBO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.5228 |
| net_win_rate | 0.4378 |
| gross_profit_factor | 0.9028 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -9.1703 |
| sortino_ratio | -4.4786 |
| max_drawdown | 0.9911 |
| cagr | -0.8929 |
| net_avg_win | 24.6668 |
| net_avg_loss | -36.7434 |
| avg_hold_time_bars | 2.6478 |
| exposure | 0.1452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
