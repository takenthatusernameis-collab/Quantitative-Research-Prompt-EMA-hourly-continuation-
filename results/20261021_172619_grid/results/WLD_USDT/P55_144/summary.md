# EMA Hourly Continuation — WLD/USDT P55_144

**Symbol:** WLD/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.9109 |
| net_win_rate | 0.5227 |
| gross_profit_factor | 1.0775 |
| gross_win_rate | 0.5227 |
| sharpe_ratio | -0.4313 |
| sortino_ratio | -0.1090 |
| max_drawdown | 0.1920 |
| cagr | -0.0526 |
| net_avg_win | 80.4994 |
| net_avg_loss | -96.7926 |
| avg_hold_time_bars | 17.8247 |
| exposure | 0.2495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
