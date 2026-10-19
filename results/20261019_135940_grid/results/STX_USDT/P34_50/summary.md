# EMA Hourly Continuation — STX/USDT P34_50

**Symbol:** STX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 866 |
| net_profit_factor | 0.4113 |
| net_win_rate | 0.4376 |
| gross_profit_factor | 0.8435 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -8.4776 |
| sortino_ratio | -3.5265 |
| max_drawdown | 0.9890 |
| cagr | -0.8301 |
| net_avg_win | 18.2201 |
| net_avg_loss | -34.4787 |
| avg_hold_time_bars | 2.8868 |
| exposure | 0.1131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
