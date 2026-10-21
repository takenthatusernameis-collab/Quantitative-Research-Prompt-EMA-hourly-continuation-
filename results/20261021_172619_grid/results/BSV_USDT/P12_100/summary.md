# EMA Hourly Continuation — BSV/USDT P12_100

**Symbol:** BSV/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.6047 |
| net_win_rate | 0.4316 |
| gross_profit_factor | 0.7798 |
| gross_win_rate | 0.4316 |
| sharpe_ratio | -3.7951 |
| sortino_ratio | -1.2147 |
| max_drawdown | 0.7618 |
| cagr | -0.4286 |
| net_avg_win | 52.2398 |
| net_avg_loss | -65.6094 |
| avg_hold_time_bars | 24.2129 |
| exposure | 0.5635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
