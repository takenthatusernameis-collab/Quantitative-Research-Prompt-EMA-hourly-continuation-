# EMA Hourly Continuation — WOO/USDT P12_144

**Symbol:** WOO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.7775 |
| net_win_rate | 0.4947 |
| gross_profit_factor | 1.0308 |
| gross_win_rate | 0.5032 |
| sharpe_ratio | -1.9565 |
| sortino_ratio | -0.6035 |
| max_drawdown | 0.5467 |
| cagr | -0.2466 |
| net_avg_win | 75.9974 |
| net_avg_loss | -95.7028 |
| avg_hold_time_bars | 31.7463 |
| exposure | 0.6825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
