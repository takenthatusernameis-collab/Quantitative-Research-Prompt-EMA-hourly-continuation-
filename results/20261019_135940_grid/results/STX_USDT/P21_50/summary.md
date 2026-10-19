# EMA Hourly Continuation — STX/USDT P21_50

**Symbol:** STX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 930 |
| net_profit_factor | 0.5304 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.9293 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -6.2101 |
| sortino_ratio | -2.6596 |
| max_drawdown | 0.9646 |
| cagr | -0.7272 |
| net_avg_win | 24.8119 |
| net_avg_loss | -41.6464 |
| avg_hold_time_bars | 4.8828 |
| exposure | 0.2055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
