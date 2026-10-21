# EMA Hourly Continuation — KAS/USDT P20_26

**Symbol:** KAS/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 140 |
| net_profit_factor | 0.9528 |
| net_win_rate | 0.5714 |
| gross_profit_factor | 1.3220 |
| gross_win_rate | 0.5714 |
| sharpe_ratio | -0.1501 |
| sortino_ratio | -0.0260 |
| max_drawdown | 0.1345 |
| cagr | -0.0138 |
| net_avg_win | 86.4402 |
| net_avg_loss | -120.9681 |
| avg_hold_time_bars | 5.0214 |
| exposure | 0.0320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
