# EMA Hourly Continuation — KSM/USDT P21_144

**Symbol:** KSM/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.6953 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.8648 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -2.1869 |
| sortino_ratio | -0.5611 |
| max_drawdown | 0.5015 |
| cagr | -0.2283 |
| net_avg_win | 72.2766 |
| net_avg_loss | -89.1896 |
| avg_hold_time_bars | 40.5474 |
| exposure | 0.6027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
