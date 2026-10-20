# EMA Hourly Continuation — EUL/USDT P12_89

**Symbol:** EUL/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 750 |
| net_profit_factor | 0.4852 |
| net_win_rate | 0.4400 |
| gross_profit_factor | 0.6951 |
| gross_win_rate | 0.4427 |
| sharpe_ratio | -5.0871 |
| sortino_ratio | -1.9402 |
| max_drawdown | 0.9109 |
| cagr | -0.6131 |
| net_avg_win | 25.9300 |
| net_avg_loss | -41.9900 |
| avg_hold_time_bars | 15.0053 |
| exposure | 0.5115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
