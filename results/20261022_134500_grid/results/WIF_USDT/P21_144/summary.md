# EMA Hourly Continuation — WIF/USDT P21_144

**Symbol:** WIF/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.6670 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.9027 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -3.0790 |
| sortino_ratio | -0.9939 |
| max_drawdown | 0.6988 |
| cagr | -0.3766 |
| net_avg_win | 56.3481 |
| net_avg_loss | -74.5200 |
| avg_hold_time_bars | 21.4118 |
| exposure | 0.5129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
