# EMA Hourly Continuation — AAVE/USDT P89_144

**Symbol:** AAVE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.4811 |
| net_win_rate | 0.4696 |
| gross_profit_factor | 0.8561 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -4.3670 |
| sortino_ratio | -1.3730 |
| max_drawdown | 0.8143 |
| cagr | -0.4834 |
| net_avg_win | 32.3601 |
| net_avg_loss | -59.5555 |
| avg_hold_time_bars | 4.9534 |
| exposure | 0.1112 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
