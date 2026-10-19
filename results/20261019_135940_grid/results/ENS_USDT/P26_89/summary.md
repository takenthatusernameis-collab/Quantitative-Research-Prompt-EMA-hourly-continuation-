# EMA Hourly Continuation — ENS/USDT P26_89

**Symbol:** ENS/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.6458 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 1.0156 |
| gross_win_rate | 0.5062 |
| sharpe_ratio | -3.8627 |
| sortino_ratio | -1.4618 |
| max_drawdown | 0.8524 |
| cagr | -0.5050 |
| net_avg_win | 42.3276 |
| net_avg_loss | -63.9353 |
| avg_hold_time_bars | 10.1259 |
| exposure | 0.3328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
