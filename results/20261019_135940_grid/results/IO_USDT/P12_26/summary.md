# EMA Hourly Continuation — IO/USDT P12_26

**Symbol:** IO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1337 |
| net_profit_factor | 0.5623 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.9229 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -8.3898 |
| sortino_ratio | -4.4390 |
| max_drawdown | 0.9944 |
| cagr | -0.8891 |
| net_avg_win | 20.8719 |
| net_avg_loss | -31.3347 |
| avg_hold_time_bars | 2.8684 |
| exposure | 0.1857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
