# EMA Hourly Continuation — CETUS/USDT P12_20

**Symbol:** CETUS/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1482 |
| net_profit_factor | 0.4609 |
| net_win_rate | 0.4197 |
| gross_profit_factor | 1.0306 |
| gross_win_rate | 0.4467 |
| sharpe_ratio | -11.8346 |
| sortino_ratio | -6.4205 |
| max_drawdown | 0.9997 |
| cagr | -0.9622 |
| net_avg_win | 13.7391 |
| net_avg_loss | -21.5618 |
| avg_hold_time_bars | 2.3077 |
| exposure | 0.1548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
