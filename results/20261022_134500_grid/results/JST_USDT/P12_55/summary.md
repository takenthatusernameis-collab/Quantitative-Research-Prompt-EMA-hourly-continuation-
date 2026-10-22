# EMA Hourly Continuation — JST/USDT P12_55

**Symbol:** JST/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 801 |
| net_profit_factor | 0.3065 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.9190 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -7.8169 |
| sortino_ratio | -3.0978 |
| max_drawdown | 0.9823 |
| cagr | -0.7967 |
| net_avg_win | 12.2618 |
| net_avg_loss | -31.6797 |
| avg_hold_time_bars | 11.2871 |
| exposure | 0.4091 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
