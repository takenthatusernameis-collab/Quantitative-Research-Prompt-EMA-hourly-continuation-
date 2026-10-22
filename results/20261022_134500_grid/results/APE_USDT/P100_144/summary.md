# EMA Hourly Continuation — APE/USDT P100_144

**Symbol:** APE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.4256 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.8314 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -5.4404 |
| sortino_ratio | -1.7953 |
| max_drawdown | 0.8894 |
| cagr | -0.5839 |
| net_avg_win | 26.3570 |
| net_avg_loss | -52.8445 |
| avg_hold_time_bars | 3.7919 |
| exposure | 0.0936 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
