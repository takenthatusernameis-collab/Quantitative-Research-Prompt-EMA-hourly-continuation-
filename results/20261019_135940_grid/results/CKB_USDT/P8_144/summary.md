# EMA Hourly Continuation — CKB/USDT P8_144

**Symbol:** CKB/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.6866 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9628 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -2.4317 |
| sortino_ratio | -0.7014 |
| max_drawdown | 0.5724 |
| cagr | -0.2854 |
| net_avg_win | 61.2085 |
| net_avg_loss | -83.4235 |
| avg_hold_time_bars | 41.0047 |
| exposure | 0.7865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
