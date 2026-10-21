# EMA Hourly Continuation — ZRX/USDT P100_144

**Symbol:** ZRX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.6876 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 1.0018 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -2.0325 |
| sortino_ratio | -0.5055 |
| max_drawdown | 0.4618 |
| cagr | -0.2063 |
| net_avg_win | 64.5944 |
| net_avg_loss | -94.5765 |
| avg_hold_time_bars | 5.8729 |
| exposure | 0.0798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
