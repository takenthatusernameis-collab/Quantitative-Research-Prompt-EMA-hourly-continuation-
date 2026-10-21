# EMA Hourly Continuation — TRX/USDT P89_144

**Symbol:** TRX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 211 |
| net_profit_factor | 0.4091 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9552 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -3.7553 |
| sortino_ratio | -0.8018 |
| max_drawdown | 0.6095 |
| cagr | -0.3063 |
| net_avg_win | 40.7893 |
| net_avg_loss | -93.2996 |
| avg_hold_time_bars | 9.0000 |
| exposure | 0.0863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
