# EMA Hourly Continuation — WLD/USDT P89_144

**Symbol:** WLD/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 226 |
| net_profit_factor | 0.8780 |
| net_win_rate | 0.5221 |
| gross_profit_factor | 1.0822 |
| gross_win_rate | 0.5221 |
| sharpe_ratio | -0.5725 |
| sortino_ratio | -0.1240 |
| max_drawdown | 0.1635 |
| cagr | -0.0573 |
| net_avg_win | 83.9880 |
| net_avg_loss | -104.5177 |
| avg_hold_time_bars | 9.3009 |
| exposure | 0.0955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
