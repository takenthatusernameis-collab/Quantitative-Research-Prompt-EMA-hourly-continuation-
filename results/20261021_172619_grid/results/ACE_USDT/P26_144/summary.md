# EMA Hourly Continuation — ACE/USDT P26_144

**Symbol:** ACE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.7945 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 0.9618 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -1.2962 |
| sortino_ratio | -0.3364 |
| max_drawdown | 0.3637 |
| cagr | -0.1450 |
| net_avg_win | 77.3963 |
| net_avg_loss | -93.4082 |
| avg_hold_time_bars | 32.4715 |
| exposure | 0.4893 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
