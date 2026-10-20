# EMA Hourly Continuation — SLP/USDT P12_34

**Symbol:** SLP/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1436 |
| net_profit_factor | 0.4657 |
| net_win_rate | 0.4123 |
| gross_profit_factor | 0.8786 |
| gross_win_rate | 0.4331 |
| sharpe_ratio | -10.9451 |
| sortino_ratio | -5.8802 |
| max_drawdown | 0.9993 |
| cagr | -0.9454 |
| net_avg_win | 14.7138 |
| net_avg_loss | -22.1609 |
| avg_hold_time_bars | 4.0592 |
| exposure | 0.2650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
