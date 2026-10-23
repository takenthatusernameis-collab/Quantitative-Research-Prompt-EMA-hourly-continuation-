# EMA Hourly Continuation — ORBS/USDT P21_144

**Symbol:** ORBS/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.5917 |
| net_win_rate | 0.4388 |
| gross_profit_factor | 0.9055 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -4.8321 |
| sortino_ratio | -1.5852 |
| max_drawdown | 0.8606 |
| cagr | -0.5372 |
| net_avg_win | 51.6518 |
| net_avg_loss | -68.2473 |
| avg_hold_time_bars | 22.5960 |
| exposure | 0.5618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
