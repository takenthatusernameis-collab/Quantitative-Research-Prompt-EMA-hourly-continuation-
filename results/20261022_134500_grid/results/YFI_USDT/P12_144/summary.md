# EMA Hourly Continuation — YFI/USDT P12_144

**Symbol:** YFI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.5821 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9618 |
| gross_win_rate | 0.4962 |
| sharpe_ratio | -3.7291 |
| sortino_ratio | -1.2012 |
| max_drawdown | 0.7750 |
| cagr | -0.4406 |
| net_avg_win | 42.1725 |
| net_avg_loss | -67.6541 |
| avg_hold_time_bars | 28.5418 |
| exposure | 0.6794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
