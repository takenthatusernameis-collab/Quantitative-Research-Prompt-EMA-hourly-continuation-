# EMA Hourly Continuation — KAS/USDT P20_34

**Symbol:** KAS/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.9144 |
| net_win_rate | 0.5618 |
| gross_profit_factor | 1.2705 |
| gross_win_rate | 0.5618 |
| sharpe_ratio | -0.4276 |
| sortino_ratio | -0.1048 |
| max_drawdown | 0.2230 |
| cagr | -0.0496 |
| net_avg_win | 80.5964 |
| net_avg_loss | -113.0171 |
| avg_hold_time_bars | 5.0424 |
| exposure | 0.0649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
