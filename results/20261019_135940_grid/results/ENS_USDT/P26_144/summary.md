# EMA Hourly Continuation — ENS/USDT P26_144

**Symbol:** ENS/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.6213 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9161 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -3.0330 |
| sortino_ratio | -0.9402 |
| max_drawdown | 0.6964 |
| cagr | -0.3636 |
| net_avg_win | 47.3776 |
| net_avg_loss | -71.1065 |
| avg_hold_time_bars | 22.6119 |
| exposure | 0.5005 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
